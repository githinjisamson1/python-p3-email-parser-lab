# your code goes here!

# import module
import re


class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # considering comma/whitespace character
        pattern = r"[,\s]"
        regex = re.compile(pattern)
        match = regex.split(self.email_addresses)
        uniqueAddresses = list(set(match))
        sortedAddresses = sorted(uniqueAddresses)
        return sortedAddresses


email_addresses = "john@doe.com, person@somewhere.org"
parser = EmailAddressParser(email_addresses)

print(parser.parse())

# => ["john@doe.com", "person@somewhere.org"]

email_addresses2 = "john@doe.com person@somewhere.org"
parser2 = EmailAddressParser(email_addresses2)
result2 = parser2.parse()
print(result2)
