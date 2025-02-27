# ...existing code...

if __name__ == "__main__":
    # Create the course generator
    generator = CybersecurityCourseGenerator()
    
    # Load user profile from a file
    generator.load_user_profile('/home/xface/repos/git_test/user_profile.json')
    
    # Generate personalized course
    course = generator.generate_personalized_course()
    
    # Save personalized course to a file
    generator.save_personalized_course(course, '/home/xface/repos/git_test/personalized_course.json')
    
    # Generate summary
    summary = generator.generate_course_summary(course)
    
    print(summary)
