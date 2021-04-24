import axios from 'axios'
export const HTTP = axios.create({
  baseURL: 'http://eventrunner.1gb.ru/'
})
