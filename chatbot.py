import openai
from dotenv import load_dotenv
load_dotenv()
import os
import sys
from getTextFromUrl import getTextFromUrl
from writeToDocx import writeToDocx
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to load the text and pass it to the model
def getAnswerFrontext(text, jobDescription):
    # Prepare prompt with text content
    prompt = f"""
    You are provided with the following resume:
    '{text}'
    and job description is '{jobDescription} '
    Based on this resume and job description, generate a cover letter 
    """
    
    # Use OpenAI's completion API to get an answer based on the text
    print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # You can use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Return the answer
    return response
webpage_text = getTextFromUrl("https://profile.amitg.pro")
jobDescription = """
Cloud Architecture Design: Produce and maintain cloud reference architecture documents for secure, scalable, and complex cloud-based applications. Ensure considerations for data privacy, access controls, and encryption.
Consultation: Consult with cloud engineering teams to ensure compliance with cloud reference architecture and deployment standards.
Migration Strategies: Develop strategies for migrating on-premises applications/solutions to the cloud.
Evaluation: Evaluate cloud solution designs for best practices, cost-effectiveness, scalability, and security. Recommend alternative designs when necessary.
Best Practices: Define and document best practices for cloud administration, including deployment, monitoring, and alerting.
Technical Audits: Conduct technical audits of existing cloud deployments to ensure adherence to current architecture standards.
Cost Management: Collaborate with the cloud FinOps team to identify cost reduction opportunities and develop cost-saving strategies.
Trends and Innovations: Stay updated on cloud technology trends to make informed decisions and maintain competitive edge.
Troubleshooting: Lead troubleshooting efforts during cloud-related outages.
"""
answer = getAnswerFrontext(webpage_text, sys.argv[1])

print("Answer:", answer)
writeToDocx("cover-letter.docx", answer.choices[0].message["content"])
