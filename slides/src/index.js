import Reveal from 'reveal.js';
import RevealMarkdown from 'reveal.js/plugin/markdown/markdown.esm.js';
import RevealHighlight from 'reveal.js/plugin/highlight/highlight.esm.js';
import RevealMath from 'reveal.js/plugin/math/math.js';
import '../node_modules/reveal.js/plugin/highlight/monokai.css';
import '../node_modules/reveal.js/dist/reveal.css';
import '../node_modules/reveal.js/dist/theme/black.css';
import './style.scss';

let deck = new Reveal({
  plugins: [
    RevealMarkdown,
    RevealHighlight,
    RevealMath,
  ],
});

deck.initialize({
  controlsTutorial: false,
  hash: true,
  respondToHashChanges: true,
});
