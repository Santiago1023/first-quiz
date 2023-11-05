import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT name, species, age FROM animals WHERE animal_id NOT IN (SELECT pet_id FROM people_animals);

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(peopleAge)
FROM (SELECT people.age AS peopleAge, animals.age as animalAge FROM (people_animals JOIN animals ON people_animals.pet_id = animal_id) JOIN people ON people_animals.owner_id = person_id)
WHERE animalAge > peopleAge;
"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT people_name, animals.name as animals_name, species
FROM animals JOIN (
    SELECT person_id, people.name as people_name, pet_id
    FROM people JOIN people_animals ON person_id = owner_id
    WHERE name = "bessie"
)
ON animals.animal_id = pet_id
WHERE pet_id NOT IN (SELECT pet_id FROM people_animals WHERE owner_id <> person_id)
"""