#!/usr/bin/node

let name;
const lang = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
/* for (name = 0; name < 3; name++) {
 * console.log(lang[name]);
 } */

for (name in lang) { console.log(lang[name]); }
