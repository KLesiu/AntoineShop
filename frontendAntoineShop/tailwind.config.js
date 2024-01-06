/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      width: {
        'xl':'26rem',
        '2xl': '32rem',
        '3xl': '48rem',
      },
    },
  },
  plugins: [],
}