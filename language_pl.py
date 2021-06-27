"""Polish Language Set"""

import subprocess


class LanguagePL:

    def interface_program(self, start):
        if start == 1:
            subprocess.run("clear")
            print("\nifconfig zainstalowano pomyślnie [+] \n")
        if start == 2:
            subprocess.run("clear")
            print("ifconfig [-]")
            print("\nInstalacja pakietu net-tools!\n")
        if start == 3:
            subprocess.run("clear")
            print("\n\nNiestety nie można zainstalować pakietu net-tools.\n\n")

    def print_interfaces(self):
        subprocess.run("clear")
        print("Aby móc zmienić adres mac interfejsu musisz uruchomić program z uprawnieniami root, lub program"
              " za pierwszym uruchomieniem niezadziała.\n")
        print("Lista dostępnych interfejsów sieciowych:\n")

    def chosen_dec(self):
        print("Musisz podać liczbę!!")

    def chosen_interface(self):
        print("Nie ma takiego interfejsu !!")

    def mac_changer(self, interface, mac):
        subprocess.run("clear")
        print("Dokonujemy zmiany w interfejsie sieciowym:\n")
        print("interface: " + interface)
        print("mac: " + mac + "\n")

        print("Wybierz jak chcesz zmienic adres mac danego interfejsu sieciowego: \n")
        print("1) Generowanie randomowowy zestaw znaków i liczb")
        print("2) Wpisz sam")
        print("e) exit\n")

    def set_random_mac_address(self, new_mac):
        print("Nowy adress mac wygenerowano: " + new_mac)

    def hand_typed_mac_address(self):
        print("\nPodaj 12 liczb, dwukropek zostanie dodany automatycznie:")

    def wrong_writed_hand_typed_mac_address(self):
        print("Wpisałeś błędnie adres mac!")

    def set_hand_type_mac_address(self, new_mac):
        print("\nRęcznie wpisany przez Ciebie adres to: " + new_mac)

    def parset_line_interfejs(self):
        return "Interfejs któremu chcemy zmienić adres mac"

    def parset_line_mac(self):
        return "Adres mac na jaki chcemy ustawić w danym interfejsie sieciowym"

    def successful_changing_mac_address(self):
        print("\nUdało się zmienić adres mac")

    def unsuccessful_changing_mac_address(self):
        print("\nNie udało się zmienić adresu mac")
