"""Main class to change the mac address of a network card interface """

import os
import re
import sys
import subprocess
import scapy.all as scapy
from random import randint
import argparse

import language_pl
import language_en

def logo():
    print("#" * 80)
    print("site: noishacking.pl")
    print("github: https://github.com/noishacking")
    print("ver: 1.0")
    print("created by: Darki")
    print("date: 27.06.2021")
    print("#" * 80)
    print("\n")

class MacChanger:

    def __init__(self):
        self.language = None
        self.language_set = None
        self.interfaces = []
        self.chosen_interface = None
        self.mac_of_chosen_interface = None
        self.new_mac = None

    def _default_language(self):
        """Gets the system language and sets it. Functions especially needed when running a program with options."""
        if re.findall("pl_PL", os.getenv('LANG')):
            self.language = "pl"
        else:
            self.language = "en"

    def _choose_language(self):
        """Menu with language selection. It is possible to choose the language, not only the system language."""
        subprocess.run("clear")
        logo()
        while True:
            print("Wybierz swój język / Choose your language: \n")
            print("1) Polski")
            print("2) English")
            print("e) exit")

            language = input("\n:> ")

            if language == "1":
                self.language = "pl"
                break
            elif language == "2":
                self.language = "en"
                break
            elif language == "e":
                print("Koniec programu / End of program")
                sys.exit()
            else:
                print("\nWybrałeś złą opcję! / You selected wrong option\n")

    def _set_default_language(self, sys_language):
        """We set the selected language, overwriting the default one """
        if sys_language == "pl":
            self.language_set = language_pl.LanguagePL()
        else:
            self.language_set = language_en.LanguageEN()

    def _interface_program(self):
        """
        Checks if the software needed to change the MAC address of the network interface is installed.
        Program I chose is ifconfig from net-tools package.
        """
        try:
            subprocess.check_output("/sbin/ifconfig")
        except FileNotFoundError:
            self.language_set.interface_program(2)
            try:
                subprocess.run(["sudo", "apt-get", "install", "net-tools"])
                self.language_set.interface_program(1)
            except subprocess.CalledProcessError:
                self.language_set.interface_program(3)

    def _list_of_interfaces(self):
        """Gets all available network interfaces and writes them to the list, except lo interface."""
        for interface in scapy.get_if_list():
            if interface == 'lo':
                pass
            else:
                self.interfaces.append(interface)

    def _print_interfaces(self):
        """List of all network interfaces"""
        self.language_set.print_interfaces()
        for i, interface in enumerate(self.interfaces, 1):
            print(str(i) + ") " + interface + ": " + scapy.get_if_hwaddr(interface))
            i += 1
        print("e) exit\n")
        self._choose_interface()

    def _choose_interface(self):
        """Save the selected interface """
        while True:
            chosen = input("-> ")
            if chosen == "e":
                sys.exit()
            else:
                if not chosen.isdecimal():
                    self.language_set.chosen_dec()
                elif int(chosen) > len(self.interfaces):
                    self.language_set.chosen_interface()
                else:
                    self.chosen_interface = self.interfaces[int(chosen) - 1]
                    break

    def _save_mac_of_chosen_interface(self):
        self.mac_of_chosen_interface = scapy.get_if_hwaddr(self.chosen_interface)

    def _random_mac_address(self):
        """
        The MAC address has 12 numbers, so the loop makes 12 turns.
        The first two numbers of the address must be even, so we check if they are, add +1 to make them even.
        At the 12th turn of the loop, stops it so that it doesn't add a colon to the end.
        If the rotation is even then a colon is added to the address.
        """
        mac = ""
        for i in range(1, 13):
            mac += str(randint(0, 9))
            if i == 2:
                if int(mac) % 2 != 0:
                    mac = self._even_number(mac)
            if i == 12:
                break
            if i % 2 == 0:
                mac += ":"
        return mac

    def _set_random_mac_address(self):
        self.new_mac = self._random_mac_address()
        self.language_set.set_random_mac_address(self.new_mac)

    @staticmethod
    def _even_number(first_part_of_mac):
        """A function that changes an odd number to an even number (in this case)"""
        modified_mac = int(first_part_of_mac)
        modified_mac += 1
        return str(modified_mac)

    def _hand_typed_mac_address(self):
        """Checking if the entered mac address is a number and if the maximum of numbers is 12 """
        self.language_set.hand_typed_mac_address()
        while True:
            numbers = input("-> ")
            if numbers.isdecimal() and len(numbers) == 12:
                return self._create_mac_address(numbers)
            else:
                self.language_set.wrong_writed_hand_typed_mac_address()

    def _create_mac_address(self, numbers):
        """
           We go through each item in the list adding the entered number to new_mac.
           For the path of the loop rotation, we must check is entered number even.
           If it is not, we change it by adding +1.
           At the twelfth loop rotation, we're going out of loop because if we did no, it would add a colon at the end.
           When the value of "i" is divisible by 2 we add a colon.
        """
        new_mac = ""
        for i, number in enumerate(numbers, 1):
            new_mac += str(number)
            if i == 2:
                if int(new_mac) % 2 != 0:
                    new_mac = self._even_number(new_mac)
            if i == 12:
                break
            if i % 2 == 0:
                new_mac += ":"
            i += 1
        return new_mac

    def _set_hand_type_mac(self):
        self.new_mac = self._hand_typed_mac_address()
        self.language_set.set_hand_type_mac_address(str(self.new_mac))

    def _mac_changer(self, interface, mac):
        """Modification menu for changing the mac address of a particular interface"""
        while True:
            self.language_set.mac_changer(interface, mac)

            mac_address = input("-> ")

            if mac_address == str(1):
                self._set_random_mac_address()
                break
            elif mac_address == str(2):
                self._set_hand_type_mac()
                break
            elif mac_address == "e":
                sys.exit()
            else:
                pass

    def _line_interface_and_mac(self):
        """The function allows to call the program in the console with options"""
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest="interface", help=self.language_set.parset_line_interfejs())
        parser.add_argument("-m", "--mac", dest="mac", help=self.language_set.parset_line_mac())
        options = parser.parse_args()

        if options.interface in self.interfaces:
            self.chosen_interface = options.interface

        if options.mac is not None:
            if options.mac.isdecimal() and len(options.mac) == 12:
                self.new_mac = self._create_mac_address(options.mac)

    def _changing_mac_address(self, mac, interface):
        """Function responsible for changing the MAC address"""
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])

        if scapy.get_if_hwaddr(self.chosen_interface) != self.mac_of_chosen_interface:
            self.language_set.successful_changing_mac_address()
        else:
            self.language_set.unsuccessful_changing_mac_address()

    def run(self):
        self._default_language()
        self._set_default_language(self.language)
        self._interface_program()
        self._list_of_interfaces()
        self._line_interface_and_mac()

        if self.chosen_interface is None:
            self._choose_language()
            self._set_default_language(self.language)
            self._print_interfaces()
            self._save_mac_of_chosen_interface()
            self._mac_changer(self.chosen_interface, self.mac_of_chosen_interface)

        self._changing_mac_address(self.new_mac, self.chosen_interface)
