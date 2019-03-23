// var railway = require('railway-api')
// railway.setApikey('70bus84o7i')
const exec = require("child_process").exec;
const request = require('request')
const fs = require('fs')

const http = require('http');

s = "https://api.railwayapi.com/v2/route/train/12621/apikey/70bus84o7i/"

const hts = http.createServer(function(req,res){
	// fs.readFile('index.html', function(error, data){
	// 	if(error) throw error;
	// 	res.end(data);
	// })
}).listen(4000);

function scanResponseCode(responseCode, callback){
	if(responseCode == 200){
		callback(null);
	}else if(responseCode == 401){
		callback("error");
	}else{
		callback("error");
	}
}

function toTitleCase(str) {
        return str.replace(
            /\w\S*/g,
            function(txt) {
                return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
            }
        );
    }
function getTrain(trainNo, callback){
      request(`https://api.railwayapi.com/v2/route/train/${trainNo}/apikey/70bus84o7i/`, function(err, res){
        if(!err){
        	// console.log(res);
        	stations = []
        	let data = res.body.split('"route":')[1]
        	// console.log(data);
        	let data1 = data.split('"station":')
        	for(let i = 1; i < data1.length; i ++){
        		let name = data1[i].split('"name":')[1];
        		let final_name = name.split('"')[1];
        		let pre_final_name = final_name.split(' JN')[0];
        		let full_final_name = pre_final_name.split(' CANTT')[0];
        		full_final_name = toTitleCase(full_final_name);
        		stations.push(full_final_name)
        		// console.log(final_name);
        		// console.log(name);
        	}
        	// console.log(stations);
        	callback(false, stations);
        	// console.log(stations)
        }
      })
    }

const io = require('socket.io')(hts);

io.on('connection', function(socket) {
   console.log('A user connected');

   socket.on('train_no', function(res){
   	getTrain(res, function(error, stations){
   		input = '';
   		for(let i = 0; i < stations.length; i++){
   			input += stations[i] + '\n';
   		}
   		input += 'exit\n';
   		fs.writeFileSync('input.txt', input);
   		var child = exec('python red_zone.py < input.txt', {maxBuffer: 1024 * 2}, function(err, stdout,stderr){
			if(err) throw err;
			if(stderr) console.log(stderr);
			output = stdout.split(' ');
			socket.emit('get_path_data', output[0], output[1]);
			console.log(stdout)
		})
   		console.log(stations);
   	})
   	// console.log(res);
   })
   //Whenever someone disconnects this piece of code executed
   socket.on('disconnect', function () {
      console.log('A user disconnected');
   });
});


// getTrain(12621, function(err, res){
// 	// console.log(res);
// });