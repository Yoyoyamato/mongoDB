// Inserting
db.students.insertOne({name: "Jack", major: "Biology", gpa: 3.5})
db.students.insertOne({name: "Claire", major: "Marketing", gpa: 3.7, awards: ["Valedictorian", "Summa Cum Laude"]} )
db.students.insertOne({name: "Evan", major: "Astronomy", gpa: 3.7, grades: [90, 88, 95, 78] } )
db.students.insertOne({name: "Kate", major: "Sociology", gpa: 3.2, contact: {phone: "333-3333", email: "student@school.edu"}})
db.students.insertOne({name: "Phil", major: "Chemistry", gpa: 2.5, startdate: new Date("2012-08-23")})
db.students.insertOne({_id: 4, name: "John", major: "Biology", gpa: 3.2})
db.students.insertMany([
     {name: "Mike", major: "Computer Science", gpa: 2.7},
     {name: "Andrea", major: "Math", gpa: 4.0, awards: ["Summa Cum Laude"]}
])

////////////////////////////////////////////////////////////
///////////////////// Practice Sets ////////////////////////
////////////////////////////////////////////////////////////


// Find all students

// Find the first 3 students

// Find all students and sort by name in ascending order

// Find all students and sort by name in ascending order

// Find all biology majors

// Find all student's with a phone number 333-3333

// Find all biology majors named Jack

// Final all students who are chemistry majors or named Jack

// Final all students with a gpa above 3.5

// Find all students with a gpa less than or equal to 3.2
                // $eq, $ne, $lt, $lte, $gt, $gte

// Find all students with names in the array
  // $in, $nin

// Find all students who have awards
         // false

// Find all db entries where the name is a string
// Type list - https://docs.mongodb.com/manual/reference/bson-types/


// Find all students who's first grade is a 90

// Find all students who have a grade greater than 80

// Find all students who have 4 grades recorded



