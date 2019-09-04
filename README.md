# PyInputCheck
 Various Functions to Validate user inputs (int, yes/no, IP addresses) and check IP address strings.

int_input() returns an integer value after the user has entered a valid integer

yes_no_input() returns a boolean value when a user has entered a valid input (y/yes/n/no). Not case sensitive.

ip_input() returns a string once the user inputs a valid IP address. Default is IPv4.
ipv4_input() and ipv6_input() check for their respective lengths.

ip_check() returns a boolean value as to whether or not the string parameter is a valid IP address. Default is IPv4.
ipv4_check() and ipv6_check() check for their respective lengths.