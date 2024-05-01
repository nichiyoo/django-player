/** @type {import('tailwindcss').Config} */
import { fontFamily } from 'tailwindcss/defaultTheme';

module.exports = {
	content: ['./templates/**/*.html', './project/**/*.py'],
	theme: {
		extend: {
			colors: {
				primary: '#FFB340',
				secondary: '#ffdba5',
				tertiary: '#6E3E0D',
			},
			fontFamily: {
				serif: ['Merriweather', ...fontFamily.serif],
			},
			animation: {
				rotate: 'spin 15s linear infinite',
			},
		},
	},
	plugins: [require('@tailwindcss/forms')],
};
