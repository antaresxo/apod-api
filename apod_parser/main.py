import apod_object_parser

# Replace with your actual API key
#API_KEY = "DEMO_KEY"
API_KEY = "ElpzBxuXHDCzOrvrtwYYlSQa3nCAgaWcsgC4hRPr" 
# pwease use your own key >.<

def main():
    print("test omg omg omg ")

    # Fetch data using the local server
    response = apod_object_parser.get_data(API_KEY)

    # Parse response
    title = apod_object_parser.get_title(response)
    explanation = apod_object_parser.get_explaination(response)
    date = apod_object_parser.get_date(response)
    hd_url = apod_object_parser.get_hdurl(response)

    # Print parsed data
    print(f"Title: {title}")
    print(f"Explanation: {explanation}")
    print(f"Date: {date}")
    print(f"HD Image URL: {hd_url}")

    # Download the image
    apod_object_parser.download_image(hd_url, date)
    print(f"Image downloaded as {date}.jpg")


if __name__ == '__main__':
    main()