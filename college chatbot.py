import sys 

college_data = {
    "50-70": [
        {"name": "Seacom Skills University", "fee": "INR 83,000"},
        {"name": "Accurate Institute of Management and Technology, Noida", "fee": "INR 1.23 Lakhs"},
        {"name": "Terna Engineering College", "fee": "INR 1.30 Lakhs"},
        {"name": "Pallavi Engineering College", "fee": "INR 55,000 to INR 65,000"},
        {"name": "Marwadi University", "fee": "INR 98,000"},
        {"name": "RK University", "fee": "INR 76,500"},
        {"name": "Dr. Subhash Technical Campus (DSTC), Junagadh", "fee": "INR 77,175"},
        {"name": "B.H.Gardi College of Engineering & Technology, Rajkot", "fee": "INR 93,000"},
        {"name": "People’s University", "fee": "INR 80,000"},
        {"name": "Sir Padampat Singhania University (SPSU)", "fee": "INR 1.70 Lakhs"},
        {"name": "The ICFAI University, Jaipur", "fee": "INR 1.20 Lakhs"}
    ],
    "70-80": [
        {"name": "Maharishi Markandeshwar (Deemed to be University), Ambala", "fee": "INR 1.42 Lakhs"},
        {"name": "SAGE University, Indore", "fee": "INR 60,000"},
        {"name": "Arya Group of Colleges, Jaipur", "fee": "INR 1.05 Lakhs"},
        {"name": "Assam Downtown University, Guwahati", "fee": "INR 1.10 Lakhs"},
        {"name": "Symbiosis University of Applied Sciences, Indore", "fee": "INR 2.60 Lakhs"},
        {"name": "Glocal University, Saharanpur", "fee": "INR 95,000"},
        {"name": "Global Research Institute of Management and Technology, Haryana", "fee": "INR 85,200"},
        {"name": "Satyam Institute, Amritsar", "fee": "INR 60,000 to INR 2.40 Lakhs"},
        {"name": "GITAM (Deemed to be University), Vishakhapatnam", "fee": "INR 9.20 Lakhs to 14.90 Lakhs"},
        {"name": "Nehru Institute of Technology, Coimbatore", "fee": "INR 2.00 Lakhs"}
    ],
    "80-85": [
        {"name": "Ramaiah Institute of Technology", "fee": "Varies"},
        {"name": "BMS College of Engineering", "fee": "Varies"},
        {"name": "Bangalore Institute of Technology", "fee": "Varies"},
        {"name": "Dayananda Sagar College of Engineering", "fee": "Varies"},
        {"name": "Nitte Meenakshi Institute of Technology", "fee": "Varies"},
        {"name": "MVJ College of Engineering", "fee": "Varies"},
        {"name": "PES University", "fee": "Varies"},
        {"name": "New Horizon College of Engineering", "fee": "Varies"},
        {"name": "Reva University", "fee": "Varies"},
        {"name": "Christ University", "fee": "Varies"}
    ],
    "86-90": [
        {"name": "NIT agartala", "fee": "INR 1.51 lakhs"},
        {"name": "NIT Meghalaya", "fee": "INR 1.55 lakhs"},
        {"name": "NIT Raipur ", "fee": "INR 1.64 lakhs"},
        {"name": "NIT Jalandar", "fee": "INR 1.8 lakhs"},
        {"name": "NIT Goa", "fee": "INR 1.33 lakhs"},
        {"name": "NIT Puducherry", "fee": "INR 1.45 lakhs"},
        {"name": "NIT Hamipur", "fee": "INR 1.8 lakhs"},
    ],
    "91-95": [
        {"name": "National Institute of Electronics and Information Technology, Aurangabad", "fee": "Varies"},
        {"name": "Chhattisgarh Swami Vivekanand Technical University, Bhilai", "fee": "Varies"},
        {"name": "Central University of Jammu, Jammu ", "fee": "Varies"},
        {"name": "Mizoram University, Aizawl", "fee": "Varies"},
        {"name": "Birla Institute of Technology, Patna", "fee": "Varies"},
        {"name": "LMNIIT Rajasthan", "fee": "Varies"},
        {"name": "MIT", "fee": "Varies"},
    ],
    "95-99.99": [
        {"name": "all major IIT's", "fee": "varies"},
    ]
}

def greet_user():
    print("Welcome to the College Admission Chatbot.")
    user_name = input("What is your name? ")
    return user_name

def ask_jee_exam():
    response = input("Have you taken the JEE exam? (yes/no) ").strip().lower()
    return response

def ask_percentile():
    percentile = input("Please share your JEE percentile: ").strip()
    try:
        percentile = float(percentile)
    except ValueError:
        print("Invalid input. Please enter a number for the percentile.")
        return ask_percentile()
    return percentile

def suggest_colleges(percentile):
    if 50 <= percentile < 70:
        options = college_data["50-70"]
    elif 70 <= percentile < 80:
        options = college_data["70-80"]
    elif 80 <= percentile <= 85:
        options = college_data["80-85"]
    elif 85 <= percentile < 90:
        options = college_data["86-90"]
    elif 90 <= percentile < 95:
        options = college_data["91-95"]
    elif 95 <= percentile <99.99:
        options = college_data["95-99.99"]
    else:
        print("I'm sorry, we don't have data for your percentile range.")
        return
    print("Based on your percentile, you can consider these colleges:")
    for college in options:
        print(f"{college['name']} - {college['fee']}")

def main():
    user_name = greet_user()
    jee_response = ask_jee_exam()
    
    if jee_response == "yes":
        percentile = ask_percentile()
        suggest_colleges(percentile)
    else:
        print("I can assist you with your JEE score only.")

    # Handling additional queries
    while True:
        more_help = input("Do you have any other questions? (yes/no) ").strip().lower()
        if more_help == "no":
            print("Thank you for using the College Admission Chatbot. Goodbye!")
            break
        elif more_help == "yes":
            jee_response = ask_jee_exam()
            if jee_response == "yes":
                percentile = ask_percentile()
                suggest_colleges(percentile)
            else:
                print("I can assist you with your JEE score only.")
        else:
            print("I didn't understand that. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    main()