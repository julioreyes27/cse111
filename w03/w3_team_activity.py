# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
 
def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('What is your gender (M or F)? ')
    birth_str = input('What is your birhtdate (YYYY-MM-DD)?')
    pounds = float(input('What is your weight in pounds? '))
    inches = float(input('What is your height in inches? '))
 
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years = compute_age(birth_str)
    weight_kg = kg_from_lb(pounds)
    height_cm = cm_from_in(inches)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, years)
 
    # Print the results for the user to see.
    print(f'Age: {years}')
    print(f'Weight in kg: {weight_kg:.2f}')
    print(f'Height in cm: {height_cm:.2f}')
    print(f'BMI: {bmi: .2f}')
    print(f'BMR: {bmr: .2f}')


 
def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
 
    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year
 
    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
 
    return years
 
def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight_kg = pounds * 0.45359237
    return weight_kg
 
def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height_cm = inches * 2.54
    return height_cm
 
def body_mass_index(weight_kg, height_cm):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000* weight_kg / height_cm**2
    return bmi
 
def basal_metabolic_rate(gender, weight, height, years):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender== "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * years
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * years
    return bmr
main()
    
 
# Call the main function so that
# this program will start executing.