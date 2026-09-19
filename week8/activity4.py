class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # University configuration
            cls._instance.university_name = ""
            cls._instance.academic_year = ""
            cls._instance.semester = ""

        return cls._instance

    # Set university configuration
    def set_config(self, university_name, academic_year, semester):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester

    # Display university configuration
    def display_config(self):
        print("University Name:", self.university_name)
        print("Academic Year:", self.academic_year)
        print("Semester:", self.semester)


# Create three objects
config1 = UniversityConfig()
config2 = UniversityConfig()
config3 = UniversityConfig()

# Set configuration using config1
config1.set_config(
    "Yoobee College of Creative Innovation",
    "2026",
    "Semester 1"
)

# Display configuration using config2
config2.display_config()

# Check if all objects are the same instance
print(config1 is config2)
print(config2 is config3)
print(config1 is config3)