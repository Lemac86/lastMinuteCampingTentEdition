<template>
  <div class="body">
    <h1>Last Minute Camping</h1>
    <div class="h1Addon">Tent Edition</div>
    <h2>Finde deinen Zeltplatz</h2>
    <div class="d-flex gap-5">
      <div class="filterHeader text-white">Filteroptionen:</div>
      <div class="search">
        <div class="searchSymbol"><i class="bi bi-search text-white"></i></div>
        <input
          type="text"
          v-model="gesuchtesAttribut"
          name=""
          id=""
          class="searchInput"
          placeholder="Gib hier den gesuchten Campingplatz oder Ort ein..."
        />
      </div>
    </div>
    <div class="backdropContentAligning gap-5">
      <div class="extras">
        <div
          class="extrasButtonAlignment"
          v-for="extra in Object.keys(filters)"
        >
          <input
            type="checkbox"
            :id="extra"
            v-model="filters[extra as  keyof typeof filters]"
          />
          <label :for="extra" class="checkboxes ps-2">
            {{ extra.charAt(0).toUpperCase() + extra.slice(1) }}</label
          >
        </div>
        <label id="priceLabel">Preis bis </label><br /><input
          type="search"
          v-model="maxPreis"
          name="Preis"
          id="priceInput"
        /><label> € </label><br /><br />
        <div class="bewertung">
          <label id="ratingLabel">Bewertung ab</label>
          <form class="star-rating">
            <template v-for="star in [5, 4, 3, 2, 1]">
              <input
                class="radio-input"
                type="radio"
                v-model="minBewertung"
                :id="'star' + star"
                name="star-input"
                :value="star"
              />
              <label
                class="radio-label"
                :for="'star' + star"
                :title="star + ' stars'"
                >{{ star + " stars" }}</label
              >
            </template>
          </form>
        </div>
      </div>
      <div class="list">
        <div class="card py-1" v-for="element in displayedArray">
          <div class="container">
            <h5 class="mb-0 pb-0">
              <b>{{ element.ort }}</b>
            </h5>
            <div class="cardText">
              {{ element.plz }}, {{ element.straße }} {{ element.hausnummer }}
            </div>
          </div>

          <img
            :src="element.bildURL"
            alt="bildLink"
            style="height: 300px; object-fit: cover"
          />
          <div class="container">
            <h5 class="pb-0 mb-0">
              <b>{{ element.name }}</b>
            </h5>
            <div class="d-flex justify-content-between">
              <div class="cardText">
                Anzahl freier Platze: {{ element.anzahlFreierPlaetze }}
              </div>
              <div class="cardText">
                Telefonnummer: {{ element.telefonnummer }}
              </div>
            </div>
            <div class="d-flex justify-content-between">
              <div class="cardText">Bewertung: {{ element.bewertung }}</div>
              <div class="cardText">Preis: {{ element.preis }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import data from "../data.json";

const filters = ref({
  WC: false,
  dusche: false,
  spielplatz: false,
  haustiere: false,
  barrierefrei: false,
  bademöglichkeit: false,
  kiosk: false,
  WLAN: false,
  strom: false,
  waschmaschine: false,
});
const minBewertung = ref("");
const maxPreis = ref("");
const gesuchtesAttribut = ref("");
let inputArray = [
  {
    name: "Neumünster Camping",
    plz: "24536",
    ort: "Neumünster",
    straße: "Hauptstraße",
    hausnummer: "18a",
    telefonnummer: "0732764552374",
    oeffnungszeitenAnfang: "07:00",
    oeffnungszeitenEnde: "21:00",
    bewertung: "3.3",
    preis: "16.50",
    anzahlFreierPlaetze: "37",
    WC: "Ja",
    dusche: "Ja",
    spielplatz: "Ja",
    haustiere: "Ja",
    barrierefrei: "Ja",
    bademöglichkeit: "Nein",
    kiosk: "Ja",
    WLAN: "Ja",
    strom: "Ja",
    waschmaschine: "Nein",
    bildURL:
      "https://mediafiles.urlaubsguru.de/wp-content/uploads/2015/04/three-friends-camping-on-mountain-at-sunset-istock_48107094_xlarge-2.jpg",
  },
  {
    name: "Bordesholm Camping",
    plz: "24532",
    ort: "Bordesholm",
    straße: "Dorfstraße",
    hausnummer: "35",
    telefonnummer: "034765387465",
    oeffnungszeitenAnfang: "07:30",
    oeffnungszeitenEnde: "21:30",
    bewertung: "4.1",
    preis: "18.00",
    anzahlFreierPlaetze: "16",
    WC: "Ja",
    dusche: "Ja",
    spielplatz: "Ja",
    haustiere: "Ja",
    barrierefrei: "Ja",
    bademöglichkeit: "Ja",
    kiosk: "Ja",
    WLAN: "Nein",
    strom: "Nein",
    waschmaschine: "Ja",
    bildURL:
      "https://cdn.prod.v2.camping.info/media/content-service/fullwidthimage/tEnct8UtjC_7.png",
  },
  {
    name: "Neumünster Camping",
    plz: "24536",
    ort: "Neumünster",
    straße: "Hauptstraße",
    hausnummer: "18a",
    telefonnummer: "0732764552374",
    oeffnungszeitenAnfang: "07:00",
    oeffnungszeitenEnde: "21:00",
    bewertung: "3.3",
    preis: "16.50",
    anzahlFreierPlaetze: "37",
    WC: "Nein",
    dusche: "Ja",
    spielplatz: "Ja",
    haustiere: "Ja",
    barrierefrei: "Ja",
    bademöglichkeit: "Nein",
    kiosk: "Ja",
    WLAN: "Ja",
    strom: "Ja",
    waschmaschine: "Nein",
    bildURL:
      "https://mediafiles.urlaubsguru.de/wp-content/uploads/2015/04/three-friends-camping-on-mountain-at-sunset-istock_48107094_xlarge-2.jpg",
  },
  {
    name: "Bordesholm Camping",
    plz: "24532",
    ort: "Bordesholm",
    straße: "Dorfstraße",
    hausnummer: "35",
    telefonnummer: "034765387465",
    oeffnungszeitenAnfang: "07:30",
    oeffnungszeitenEnde: "21:30",
    bewertung: "4.1",
    preis: "18.00",
    anzahlFreierPlaetze: "16",
    WC: "Ja",
    dusche: "Ja",
    spielplatz: "Ja",
    haustiere: "Ja",
    barrierefrei: "Ja",
    bademöglichkeit: "Ja",
    kiosk: "Ja",
    WLAN: "Nein",
    strom: "Nein",
    waschmaschine: "Ja",
    bildURL:
      "https://cdn.prod.v2.camping.info/media/content-service/fullwidthimage/tEnct8UtjC_7.png",
  },
];

const displayedArray = computed(() =>
  inputArray.filter(
    (e) =>
      ((filters.value.WC && e.WC == "Ja") || filters.value.WC == false) &&
      ((filters.value.dusche && e.dusche == "Ja") ||
        filters.value.dusche == false) &&
      ((filters.value.spielplatz && e.spielplatz == "Ja") ||
        filters.value.spielplatz == false) &&
      ((filters.value.haustiere && e.haustiere == "Ja") ||
        filters.value.haustiere == false) &&
      ((filters.value.barrierefrei && e.barrierefrei == "Ja") ||
        filters.value.barrierefrei == false) &&
      ((filters.value.bademöglichkeit && e.bademöglichkeit == "Ja") ||
        filters.value.bademöglichkeit == false) &&
      ((filters.value.kiosk && e.kiosk == "Ja") ||
        filters.value.kiosk == false) &&
      ((filters.value.WLAN && e.WLAN == "Ja") || filters.value.WLAN == false) &&
      ((filters.value.strom && e.strom == "Ja") ||
        filters.value.strom == false) &&
      ((filters.value.waschmaschine && e.waschmaschine == "Ja") ||
        filters.value.waschmaschine == false) &&
      (!minBewertung.value ||
        parseFloat(e.bewertung) > parseFloat(minBewertung.value)) &&
      (!maxPreis.value || parseFloat(e.preis) < parseFloat(maxPreis.value)) &&
      (e.name
        .toLocaleLowerCase()
        .includes(gesuchtesAttribut.value.toLowerCase()) ||
        e.ort
          .toLocaleLowerCase()
          .includes(gesuchtesAttribut.value.toLowerCase()))
  )
);
</script>

<style>
@font-face {
  font-family: "camping-font";
  src: url(Sriracha-Regular.ttf);
}

body {
  background-image: url(gras5.jpg);
  background-size: cover;
}
h1 {
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 60px;
  padding-top: 5vh;
  position: relative;
  /* text-decoration: underline; */
}

.h1Addon {
  position: absolute;
  font-family: "camping-font";
  color: rgba(94, 116, 31, 0.9);
  text-shadow: 1px 0.5px rgba(131, 155, 23, 0.5);
  font-size: 30px;
  left: calc(100vw / 2 + 250px);
  top: 10%;
  transform: rotate(-15deg);
  text-decoration: underline;
}

h2 {
  text-align: center;
  padding-top: 8vh;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 35px;
  margin-bottom: 1vh;
  /* text-decoration: underline; */
}
.filterHeader {
  display: flex;
  padding-left: 20px;
  border-radius: 0 10px 0 0;
  align-items: center;
  width: 10vw;
  height: 2.5rem;
  background-color: rgba(131, 155, 23, 0.8);
}
.search {
  display: flex;
  justify-content: center;
  width: 75vw;
  height: 2.5rem;
}
.searchSymbol {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 5vw;
  text-align: center;
  border-radius: 10px 0 0 0;
  background-color: rgba(131, 155, 23, 0.8);
}
.searchInput {
  width: 70vw;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1rem;
  border-radius: 0 10px 0 0;
  border: none;
  padding-left: 25px;
  background-color: rgba(131, 155, 23, 0.4);
}
.searchInput:focus {
  outline: none;
}

.backdropContentAligning {
  display: flex;
  flex-direction: row;
  height: 65vh;
}
.list {
  /* margin: 0 auto; */
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  background-color: rgba(202, 205, 245, 0.5);
  width: 75vw;
  border-radius: 0 0 10px 10px;
  backdrop-filter: blur(10px);
  overflow-y: scroll;
  scrollbar-width: none;
}
/* card START */
.card {
  font-family: Arial, Helvetica, sans-serif;
  box-shadow: 6px 8px 16px 0 rgba(0, 0, 0, 0.3);
  transition: 0.3s;
  margin: 10px;
  border-radius: 5px;
}
.cardText {
  font-size: 13px;
  color: rgba(0, 0, 0, 0.7);
}
.container {
  padding: 10px;
}
img {
  border-radius: 5px 5px 0 0;
}
/* card END */
.extras {
  padding-top: 15px;
  font-size: 17px;
  font-weight: 100;
  font-family: "camping-font";

  padding-left: 10px;
  backdrop-filter: blur(10px);
  background-color: rgba(202, 205, 245, 0.5);
  border-radius: 0 0 10px 0;
  width: 10vw;
}
.extrasButtonAlignment {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}
.checkboxes {
  margin: 0;
  padding: 0;
  /* margin-bottom: 5px; */
}
label:hover {
  cursor: pointer;
}
#ratingLabel {
  padding-left: 5px;
}
#priceLabel {
  padding-left: 5px;
}
#priceInput {
  font-family: Arial, Helvetica, sans-serif;
  border-radius: 10px;
  padding-left: 10px;
  margin-right: 3px;
  border: none;
  width: 85%;
  box-shadow: inset 0 0 0 1px rgb(131, 155, 23);
  background-color: rgba(131, 155, 23, 0.4);
}
/* checkbox Layout START */
[type="checkbox"] {
  width: 1rem;
  height: 1rem;
  color: rgba(131, 155, 23, 0.75);
  vertical-align: middle;
  -webkit-appearance: none;
  background: none;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.9);
  /* transition: background 300ms; */
  cursor: pointer;
}
[type="checkbox"]::before {
  content: "";
  color: transparent;
  display: block;
  width: inherit;
  height: inherit;
  border-radius: inherit;
  border: 0;
  background-color: transparent;
  background-size: contain;
  box-shadow: inset 0 0 0 1px #ccd3d8;
}
[type="checkbox"]:checked {
  background-color: currentcolor;
}
[type="checkbox"]:checked::before {
  box-shadow: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E %3Cpath d='M15.88 8.29L10 14.17l-1.88-1.88a.996.996 0 1 0-1.41 1.41l2.59 2.59c.39.39 1.02.39 1.41 0L17.3 9.7a.996.996 0 0 0 0-1.41c-.39-.39-1.03-.39-1.42 0z' fill='%23fff'/%3E %3C/svg%3E");
}
/* checkbox Layout END */
/* Bewertung START*/
.bewertung {
  display: flex;
  flex-direction: column;
}
.star-rating {
  padding-top: 0;
  margin-top: 0;
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
}
.radio-input {
  position: fixed;
  opacity: 0;
  pointer-events: none;
}

.radio-label {
  cursor: pointer;
  font-size: 0;
  color: rgba(0, 0, 0, 0.1);
  transition: color 0.1s ease-in-out;
}

.radio-label:before {
  content: "★";
  display: inline-block;
  font-size: 32px;
}
.radio-input:checked ~ .radio-label {
  color: rgb(94, 116, 31);
}

.radio-label:hover,
.radio-label:hover ~ .radio-label {
  color: rgba(131, 155, 23, 0.5);
}

.radio-input:checked + .radio-label:hover,
.radio-input:checked + .radio-label:hover ~ .radio-label,
.radio-input:checked ~ .radio-label:hover,
.radio-input:checked ~ .radio-label:hover ~ .radio-label,
.radio-label:hover ~ .radio-input:checked ~ .radio-label {
  color: rgba(131, 155, 23, 0.75);
}
/* Bewertung END */
</style>
