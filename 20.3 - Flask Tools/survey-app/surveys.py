class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text

    def __repr__(self):
        return f"<Question: {self.question}>"
    
    def __str__(self):
        return f"Question: {self.question}\nChoices: {', '.join(self.choices)}"

class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions

satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

employee_engagement_survey = Survey(
    "Employee Engagement Survey",
    "We value your feedback. Please fill out this survey to help us improve our workplace.",
    [
        Question("Do you feel valued at work?"),
        Question("Do you have the tools and resources to do your job effectively?"),
        Question("How likely are you to recommend this company to a friend?",
                 ["Very likely", "Somewhat likely", "Not likely"]),
        Question("What can we do to improve your work experience?", allow_text=True),
        Question("How satisfied are you with your work-life balance?",
                 ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"]),
        Question("Do you feel you have opportunities for professional growth and development?",
                 ["Yes", "No", "Not sure"]),
        Question("How would you rate the communication between management and staff?",
                 ["Excellent", "Good", "Average", "Poor", "Very Poor"]),
        Question("Do you receive regular feedback on your performance?",
                 ["Yes, regularly", "Occasionally", "No, but I would like to", "No, and I don't need it"]),
        Question("What aspects of your job do you enjoy the most?", allow_text=True),
        Question("Are there any changes you would suggest for improving team collaboration?", allow_text=True),
    ]
)

product_feedback_survey = Survey(
    "Product Feedback Survey",
    "We would love to hear your thoughts on our product.",
    [
        Question("How satisfied are you with our product?",
                 ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"]),
        Question("How likely are you to recommend our product to others?",
                 ["Very likely", "Somewhat likely", "Neutral", "Somewhat unlikely", "Very unlikely"]),
        Question("What do you like most about our product?", allow_text=True),
        Question("What do you like least about our product?", allow_text=True),
        Question("Do you have any suggestions for improving our product?", allow_text=True),
        Question("How often do you use our product?",
                 ["Daily", "Weekly", "Monthly", "Rarely", "Never"]),
        Question("How would you rate the value for money of our product?",
                 ["Excellent", "Good", "Average", "Poor", "Very Poor"]),
    ]
)

event_feedback_survey = Survey(
    "Event Feedback Survey",
    "Your feedback helps us make our events better. Please fill out this survey.",
    [
        Question("How satisfied were you with the event overall?",
                 ["Very satisfied", "Somewhat satisfied", "Neutral", "Somewhat dissatisfied", "Very dissatisfied"]),
        Question("How would you rate the organization of the event?",
                 ["Excellent", "Good", "Average", "Poor", "Very Poor"]),
        Question("What was your favorite part of the event?", allow_text=True),
        Question("What was your least favorite part of the event?", allow_text=True),
        Question("How likely are you to attend another event organized by us?",
                 ["Very likely", "Somewhat likely", "Neutral", "Somewhat unlikely", "Very unlikely"]),
        Question("Do you have any suggestions for future events?", allow_text=True),
        Question("How did you hear about this event?",
                 ["Email", "Social Media", "Word of Mouth", "Other"]),
        Question("Would you like to be notified about future events?",
                 ["Yes", "No"]),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "employee": employee_engagement_survey,
    "product_feedback": product_feedback_survey,
    "event_feedback": event_feedback_survey,
}
