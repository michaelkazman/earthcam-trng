const { EarthBlock } = require('./earthblock')
const { EarthChain } = require('./earthchain')

function main() {
  let earthCoin = new EarthChain();
  
  console.log("EarthCoin blockchain initializing....");
  
  earthCoin.addNewBlock(
    new EarthBlock(1, "01/06/2020", {
      sender: "Iris Ljesnjanin",
      recipient: "Cosima Mielke",
      quantity: 69
    }));
  
  earthCoin.addNewBlock(
    new EarthBlock(2, "01/07/2020", {
      sender: "Vitaly Friedman",
      recipient: "Ricardo Gimenes",
      quantity: 420
    })
  );
  
  earthCoin.addNewBlock(
    new EarthBlock(3, "01/07/2020", {
      sender: "Carleton University",
      recipient: "David Barrera",
      quantity: 42
    })
  );
  
  earthCoin.addNewBlock(
    new EarthBlock(4, "01/08/2020", {
      sender: "Michael Kazman",
      recipient: "Trevor Johns",
      quantity: 99
    })
  );
  
  earthCoin.addNewBlock(
    new EarthBlock(5, "01/08/2020", {
      sender: "Trevor Johns",
      recipient: "McDonalds",
      quantity: 3
    })
  );

  console.log(JSON.stringify(earthCoin, null, 4)); 
}  

main()