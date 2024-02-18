from textblob import TextBlob


# Function to label subjectivity level based on the subjectivity score
def subjectivity_label(subjectivity):
    if subjectivity == 0:
        return "Very Objective"
    elif subjectivity < 0.25:
        return "Objective"
    elif subjectivity < 0.5:
        return "Moderately Objective"
    elif subjectivity == 0.5:
        return "Somewhat Objective, Somewhat Subjective"
    elif subjectivity < 0.75:
        return "Moderately Subjective"
    elif subjectivity < 1:
        return "Subjective"
    else:
        return "Very Subjective"


# Function to label polarity level based on the polarity score
def polarity_label(polarity):
    if polarity == -1:
        return "Very Negative"
    elif polarity < -0.5:
        return "Negative"
    elif polarity < 0:
        return "Moderately Negative"
    if polarity == 1:
        return "Very Positive"
    elif polarity > 0.5:
        return "Positive"
    elif polarity > 0:
        return "Moderately Positive"


# Function to analyze sentiment of the given text
def analyze_sentiment(text):
    # Create a TextBlob object
    aText = TextBlob(text)

    # Get polarity and subjectivity scores
    textPolarity = aText.sentiment.polarity
    textSubjectivity = aText.sentiment.subjectivity

    # Label polarity and subjectivity levels
    polarityLabel = polarity_label(textPolarity)
    subjectivityLabel = subjectivity_label(textSubjectivity)

    # Print the analyzed text along with its polarity and subjectivity levels
    print("\n---------------------------------\n")
    print(f"Analyzed text:\n{text}")
    print(f"Polarity: {polarityLabel} ({aText.sentiment.polarity})")
    print(f"Subjectivity: {subjectivityLabel} ({aText.sentiment.subjectivity})")
    print("\n---------------------------------\n")
