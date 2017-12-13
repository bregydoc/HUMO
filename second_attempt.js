import Nightmare from 'nightmare';
const nightmare = Nightmare({ show: true });

nightmare
  .goto('https://duckduckgo.com')
  .type('#search_form_input_homepage', 'github nightmare')
  .click('#search_button_homepage')
  .wait('#r1-0 a.result__a')
  .evaluate(() => document.querySelector('#r1-0 a.result__a').href)
  .end()
  .then(console.log)
  .catch((error) => {
    console.error('Search failed:', error);
  });


const Nightmare = require('nightmare')
const nightmare = Nightmare({ show: true })

nightmare
  .goto('https://accounts.google.com/o/oauth2/auth?client_id=106735915676-jgh1pts7v6lss7l5cqdi472b7lfn78lc.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Fcore.utecsup.com%2FUTEC-Web%2Fj_spring_oauth_security_check%3Foauth_provider_type%3DGoogle2Provider&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&state=')
  .click('div#initialView > div.bdf4dc.slptg:nth-child(2)')
  .click('div#identifierNext > content.CwaK9:nth-child(3) > span.RveJvd.snByac:nth-child(1)')
  .click('input#identifierId')
  .click('div#identifierNext > div.ZFr60d.CeoRYc:nth-child(2)')
  .click('input#identifierId')
  .click('div#identifierNext > div.ZFr60d.CeoRYc:nth-child(2)')
  .click('div#passwordNext > content.CwaK9:nth-child(3)')
  .end()
    .then(function (result) {
      console.log(result)
    })
    .catch(function (error) {
      console.error('Error:', error);
    });
