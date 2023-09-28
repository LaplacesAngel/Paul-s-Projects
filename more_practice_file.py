first_name = 'paul'
last_name = 'lentz'
note = 'award: launchcode completion'

first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()
award_location = note.find(":")
print(award_location)
after_award = note[award_location+2: len(note)]
print(after_award)