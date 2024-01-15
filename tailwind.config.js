/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./templates/*.html",
		"./home/templates/*.html",
		"./programs/templates/*.html",
		"./schedule/templates/*.html",
		"./pricing/templates/*.html",
		"./announcements/templates/*.html",
	],
	theme: {
		extend: {},
	},
	plugins: [require("@tailwindcss/typography"), require("daisyui")],
};
