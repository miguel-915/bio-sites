/**
 * Award booking request intake.
 * Paste into the "Award Booking Requests" Google Sheet: Extensions > Apps Script.
 * Deploy > New deployment > Web app, Execute as: Me, Who has access: Anyone.
 * The award-booking pages on both bio sites POST their form here.
 */
const NOTIFY = 'travelsergeant@gmail.com';

// Form field name -> sheet column header
const FIELDS = {
  site: 'Site', type: 'Type', name: 'Name', email: 'Email', phone: 'Phone', instagram: 'Instagram',
  trip_type: 'Trip type', from: 'From', to: 'To', depart: 'Depart', return_date: 'Return',
  flexibility: 'Date flexibility', adults: 'Adults', children: 'Children', infants: 'Lap infants',
  cabin: 'Cabin', stops: 'Stops', bank_points: 'Bank points', other_points: 'Airline and hotel points',
  notes: 'Notes', heard: 'Heard about us', agree: 'Agreed to deposit'
};

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.website) return ok_(); // spam trap: real people never fill this hidden field
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  const byHeader = { Submitted: new Date(), Status: 'New' };
  Object.keys(FIELDS).forEach(k => { byHeader[FIELDS[k]] = String(p[k] || '').slice(0, 2000); });
  sheet.appendRow(headers.map(h => (h in byHeader ? byHeader[h] : '')));

  const trip = `${byHeader['From']} → ${byHeader['To']} · ${byHeader['Trip type']} · ${byHeader['Cabin']}`;
  const body = Object.keys(FIELDS).map(k => `${FIELDS[k]}: ${byHeader[FIELDS[k]]}`).join('\n')
    + `\n\nSheet: ${SpreadsheetApp.getActiveSpreadsheet().getUrl()}`;
  MailApp.sendEmail({
    to: NOTIFY,
    replyTo: byHeader['Email'] || NOTIFY,
    subject: `New award booking request: ${byHeader['Name']} (${trip})`,
    body: body
  });
  return ok_();
}

function ok_() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
}
