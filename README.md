# Obfuscated-Email-Extractor
Obfuscated_Email_Extractor is a Python library that can extract obfuscated email addresses from HTML and JavaScript code. The library is designed to help web developers and researchers extract email addresses that are hidden or encoded on web pages.

The main code of the library is contained in the obfuscated_email_extractor.py file. This file defines a class called ObfuscatedEmailExtractor that has a method called extract_emails. The extract_emails method takes a string of HTML or JavaScript code as input and returns a list of extracted email addresses. The method uses regular expressions to search for common email address patterns and decode obfuscated email addresses.

The obfuscated_email_extractor.py file also contains several helper functions and regular expressions that are used by the extract_emails method. These functions and regular expressions are designed to handle various types of obfuscation, such as ASCII and hexadecimal encoding, JavaScript encoding, and so on.
