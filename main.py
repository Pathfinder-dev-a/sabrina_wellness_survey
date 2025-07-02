import csv
import os
from datetime import datetime

# Define the Medicine Wheel quadrants and their questions
quadrants = {
    "Physical": [
        "How often do you engage in physical exercise? (1-5)",
        "How well do you maintain a balanced diet? (1-5)",
        "How much sleep do you get nightly? (1-5, 1=poor, 5=excellent)",
        "How often do you participate in community physical activities? (1-5)",
        "How comfortable are you in your physical environment? (1-5)"
    ],
    "Mental": [
        "How often do you engage in problem-solving activities? (1-5)",
        "How confident are you in your decision-making skills? (1-5)",
        "How often do you learn new skills or knowledge? (1-5)",
        "How well do you manage stress? (1-5)",
        "How often do you engage in creative activities? (1-5)"
    ],
    "Emotional": [
        "How connected do you feel to your community? (1-5)",
        "How often do you express your emotions openly? (1-5)",
        "How well do you handle emotional challenges? (1-5)",
        "How strong are your relationships with others? (1-5)",
        "How often do you feel a sense of belonging? (1-5)"
    ],
    "Spiritual": [
        "How often do you reflect on your purpose or values? (1-5)",
        "How connected do you feel to something greater than yourself? (1-5)",
        "How often do you practice gratitude? (1-5)",
        "How often do you engage in spiritual or cultural practices? (1-5)",
        "How at peace do you feel with your life’s direction? (1-5)"
    ]
}

# CSV file setup
csv_file = "community_survey.csv"
csv_headers = ["Timestamp", "UserID"] + [f"{quadrant}_{i+1}" for quadrant in quadrants for i in range(5)] + [f"{quadrant}_Score" for quadrant in quadrants] + ["Total_Community_Score"]

# Ensure CSV file exists with headers
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

def validate_input(response):
    try:
        score = int(response)
        if 1 <= score <= 5:
            return score
        else:
            print("Please enter a number between 1 and 5.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

def survey_user():
    user_id = input("Enter a unique User ID: ")
    responses = {}
    quadrant_scores = {}

    print("\nPlease answer the following questions on a scale of 1 to 5 (1 = Poor, 5 = Excellent):\n")

    # Collect responses for each quadrant
    for quadrant, questions in quadrants.items():
        responses[quadrant] = []
        print(f"\n{quadrant} Questions:")
        for i, question in enumerate(questions, 1):
            while True:
                response = input(f"Q{i}. {question} ")
                score = validate_input(response)
                if score is not None:
                    responses[quadrant].append(score)
                    break
        # Calculate quadrant score (sum of responses)
        quadrant_scores[quadrant] = sum(responses[quadrant])

    # Calculate total community score (sum of all quadrant scores)
    total_community_score = sum(quadrant_scores.values())

    # Prepare data for CSV
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    csv_row = [timestamp, user_id]
    for quadrant in quadrants:
        csv_row.extend(responses[quadrant])
    for quadrant in quadrants:
        csv_row.append(quadrant_scores[quadrant])
    csv_row.append(total_community_score)

    # Save to CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_row)

    # Display results
    print("\nSurvey Results:")
    for quadrant, score in quadrant_scores.items():
        print(f"{quadrant} Score: {score}/25")
    print(f"Total Community Score: {total_community_score}/100")
    print(f"\nData saved to {csv_file}")

def main():
    print("Welcome to the Medicine Wheel Community Survey")
    while True:
        survey_user()
        again = input("\nWould you like to complete another survey? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for participating!")
            break

if __name__ == "__main__":
    main()