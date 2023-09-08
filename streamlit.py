import streamlit as st


def calculate_mean(grades):
    total_grades = sum(grades)
    num_grades = len(grades)
    mean = total_grades / num_grades
    return mean


def main():
    st.title("Student Grade Calculator")
    st.write(
        "Enter the grades for each subject and click 'Calculate Mean' to get the average.")

    # Get the number of subjects from the user
    num_subjects = st.number_input(
        "Number of Subjects", min_value=1, max_value=10, step=1, value=1)

    # Create a list to store the grades
    grades = []

    # Loop through each subject to get the grades
    for subject in range(num_subjects):
        grade = st.number_input(
            f"Enter grade for Subject {subject+1}", min_value=0.0, max_value=100.0, step=0.1, value=0.0)
        grades.append(grade)

    # Calculate the mean grade
    if st.button("Calculate Mean"):
        mean_grade = calculate_mean(grades)
        st.write(f"The mean grade is: {mean_grade:.2f}")


if __name__ == '__main__':
    main()