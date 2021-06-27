"""English Language Set"""

import subprocess


class LanguageEN:

    def interface_program(self, start):
        if start == 1:
            subprocess.run("clear")
            print("\nifconfig installed successfully [+] \n")
        if start == 2:
            subprocess.run("clear")
            print("ifconfig [-]")
            print("\nInstalling the net-tools!\n")
        if start == 3:
            subprocess.run("clear")
            print("\n\nUnfortunately, the net-tools package cannot be installed.\n\n")

    def print_interfaces(self):
        subprocess.run("clear")
        print("To be able to change the MAC address of the interface you must run the program with root privileges," 
              " or the program will not work the first time you run it. \n")
        print("List of available network interfaces:\n")

    def chosen_dec(self):
        print("You must enter a number !!")

    def chosen_interface(self):
        print("There is no such interface !!")

    def mac_changer(self, interface, mac):
        subprocess.run("clear")
        print("We change mac address to the chosen interface:\n")
        print("interface: " + interface)
        print("mac: " + mac + "\n")

        print("Choose how you want to change the MAC address of a chosen network interface:\n")
        print("1) Generate a random set of characters and numbers")
        print("2) Type yourself")
        print("e) exit\n")

    def set_random_mac_address(self, new_mac):
        print("A new mac address has been generated: " + new_mac)

    def hand_typed_mac_address(self):
        print("\nEnter 12 numbers, a colon will be added automatically:")

    def wrong_writed_hand_typed_mac_address(self):
        print("You entered the MAC address incorrectly!")

    def set_hand_type_mac_address(self, new_mac):
        print("\nThe manually address you entered is: " + new_mac)

    def parset_line_interfejs(self):
        return "The interface we want to change the mac address"

    def parset_line_mac(self):
        return "The MAC address we want to set in a selected network interface "

    def successful_changing_mac_address(self):
        print("\nThe mac address has been changed")

    def unsuccessful_changing_mac_address(self):
        print("\nThe mac address could not be changed")
