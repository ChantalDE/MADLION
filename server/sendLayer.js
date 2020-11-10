var express = require('express') 
var wfs=require('geojson-to-wfs-t-2');
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const app = express();
app.use(express.json());
 
 
app.get('/', (req, res) => {
    return res.send('Received a GET HTTP method');
});
 
app.post('/', (req, res) => {
    //res.send(req.body);
    const params = {geometry_name: 'geom', layer: 'geometries', ns: 'IOT'};

    // create a stringified transaction inserting null island

    var x = wfs.Transaction(
        wfs.Insert(req.body, params),
        {
        nsAssignments: {
          IOT: 'http://www.openplans.org/'
        }
    }
    );
    //console.log(req.body);
    //console.log(x);

    //post x to geoserver

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://3.22.118.224:8080/geoserver/wfs', true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Authorization", "Basic YWRtaW46Z2Vvc2VydmVy");
    xhr.setRequestHeader("Content-Type", "application/xml");

    xhr.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            //console.log("status: ", this.status);
        }
        else{
          console.log("status: ", this.status);
        }
    }
    xhr.send(x);

   return res.send('Received a POST HTTP method');
 });
 
app.put('/', (req, res) => {
  return res.send('Received a PUT HTTP method');
});
 
app.delete('/', (req, res) => {
  return res.send('Received a DELETE HTTP method');
});
 
app.listen(3000, () =>
  console.log(`Example app listening on port 3000!`),
);