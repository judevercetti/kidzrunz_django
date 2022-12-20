/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/*html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
