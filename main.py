# Library
import phonenumbers
from phonenumbers import carrier,geocoder, timezone

# Enter number (International Format)
mobileNum = input("Enter phonenumbers with country codes: ")
mobileNum = phonenumbers.parse(mobileNum)

# Timezone of the number 
print(timezone.time_zones_for_number(mobileNum))

# Carrier of the mobile number
print(carrier.name_for_number(mobileNum, "en"))

# Geographic information of the mobile number
print(geocoder.description_for_number(mobileNum, "en"))

# Service provider
print("Service Provider: ", phonenumbers.is_possible_number(mobileNum))

# Valid number
print("Valid Number: ", phonenumbers.is_valid_number(mobileNum))