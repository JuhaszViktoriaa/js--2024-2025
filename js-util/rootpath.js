import path from 'path' //az osszes fajlt behozza
import { fileURLToPath } from 'url' //tobb fuggveny van benne

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');

export default root;