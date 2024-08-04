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
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "employee": employee_engagement_survey
}