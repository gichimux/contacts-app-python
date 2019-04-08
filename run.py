#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,number,email):
    '''
    function to create anew contact
    '''
    new_contact = Contact(fname,lname,number,email)
    return new_contact

def save_contact(contact):
    '''
    function to save contact
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    function to delete contact
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    function that finds the contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    function that checks if a contact exists by the number and returns a boolean
    '''
    return Contact.display_contacts()

def copy_the_email(number):
    '''
    function that copies the email to the clipboard
    '''
    return Contact.copy_email(number)

def main():
    print("Hello welcome to your contact list. what is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
            print("Use these shortcodes : cc - create a new contact, dc - display contacts, fc - find a contact, ex exit the conatct list ")
            short_code = input().lower()

            if short_code == 'cc':
                print("New Contact")
                print("-"* 10)

                print("First name ....")
                f_name = input()

                print ("Last Name ...")
                l_name = input()

                print("Phone Number ...")
                p_number = input()

                print("Email adress ...")
                e_address = input()

                save_contact(create_contact(f_name,l_name,p_number,e_address))#create and save new contact
