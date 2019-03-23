package personcontroller

import (
	"log"
	"models"
	"net/http"
	"encoding/json"
	"github.com/gorilla/mux"
)

var people []models.Person

func GetPeople(w http.ResponseWriter, r *http.Request) {
	log.Print("Inside the GetPeople Method")
	json.NewEncoder(w).Encode(people)
	log.Print("Completed the operations with the Get People Method")
}

func GetPerson(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	log.Print("params=", params)
	flag := false
	for _, item := range people {
		if item.ID == params["id"] {
			json.NewEncoder(w).Encode(item)
			log.Print("Found the Person Object. Returning it")
			flag = true
		} 
	}
	if !flag {
		log.Print("The Person with Person ID ", params["id"], " not found. Returning 404")
		json.NewEncoder(w).Encode(&models.ErrorMessage{Status:404, Message: "Error"})
	}
}

func CreatePerson(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
    var person models.Person
    _ = json.NewDecoder(r.Body).Decode(&person)
    person.ID = params["id"]
    people = append(people, person)
    json.NewEncoder(w).Encode(people)
}

func DeletePerson(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
    for index, item := range people {
        if item.ID == params["id"] {
            people = append(people[:index], people[index+1:]...)
            break
        }
        json.NewEncoder(w).Encode(people)
    }
}

func AddDummyPeople() {
	people = append(people, models.Person{ID: "1", Firstname: "John", Lastname: "Doe", Address: &models.Address{City: "City X", State: "State X"}})
	people = append(people, models.Person{ID: "2", Firstname: "Koko", Lastname: "Doe", Address: &models.Address{City: "City Z", State: "State Y"}})
	people = append(people, models.Person{ID: "3", Firstname: "Francis", Lastname: "Sunday"})
}