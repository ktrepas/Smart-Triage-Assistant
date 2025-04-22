#!/usr/bin/env python
# coding: utf-8

# In[2]:


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please answer yes or no.")

def triage():
    print("Welcome to Smart Triage Assistant.\nAnswer a few quick questions.")
    chest_pain = ask_yes_no("Are you experiencing chest pain?")
    difficulty_breathing = ask_yes_no("Do you have trouble breathing?")
    bleeding = ask_yes_no("Are you bleeding heavily?")
    unconscious = ask_yes_no("Is the person unconscious or non-responsive?")
    high_fever = ask_yes_no("Do you have a high fever (above 39°C / 102°F)?")
    
    score = 0
    if chest_pain or difficulty_breathing:
        score += 2
    if bleeding:
        score += 2
    if unconscious:
        score += 3
    if high_fever:
        score += 1
        
    print("\nTriage Result:")
    if score >= 5:
        print("🚨 Critical condition. Call emergency services immediately.")
    elif score >= 3:
        print("⚠️ Serious symptoms. Seek medical attention soon.")
    else:
        print("✅ Symptoms not critical. Monitor at home and rest.")

if __name__ == "__main__":
    triage()


# In[ ]:




