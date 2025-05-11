import phonenumbers
from opencage.geocoder import OpenCageGeocode

# Your OpenCage API key
API_KEY = '6e600e2f70214a3eb2875f15426d5da0'

def get_location_from_phone_number(phone_number):
    # Parse phone number using phonenumbers library
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        # Get the country code
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        
        # Initialize OpenCageGeocode with API Key
        geocoder = OpenCageGeocode(API_KEY)
        
        # Construct the query for OpenCage
        query = f"+{country_code}{national_number}"
        
        # Use OpenCage API to get geolocation data
        results = geocoder.geocode(query)
        
        if results:
            location_info = results[0]
            latitude = location_info.get('geometry', {}).get('lat')
            longitude = location_info.get('geometry', {}).get('lng')
            
            if latitude and longitude:
                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")
            else:
                print("Could not extract latitude and longitude.")
        else:
            print("No results found for the given phone number.")
    
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Accept phone number input
    phone_number = input("Enter phone number with country code (e.g., +919876543210): ")
    
    # Get and display latitude and longitude
    get_location_from_phone_number(phone_number)
