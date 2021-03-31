const { EarthBlock } = require('./earthblock')

class EarthChain {
    constructor() {
      this.blockchain = [this.startGenesisBlock()];
      this.difficulty = 3;
      this.threshold = 2;
    }
  
    startGenesisBlock() {
      return new EarthBlock(0, "01/01/2020", "Initial Block in the Chain", "0");
    }
  
    obtainLatestBlock() {
      return this.blockchain[this.blockchain.length - 1];
    }
  
    addNewBlock(newBlock) {
      // increase difficulty as blockchain grows
      if (this.blockchain.length % this.threshold == 0)
          this.difficulty++;
      // 
      newBlock.precedingHash = this.obtainLatestBlock().hash;
      newBlock.proofOfWork(this.difficulty);
      this.blockchain.push(newBlock);
    }
  
    checkChainValidity() {
      for (let i = 1; i < this.blockchain.length; i++) {
        const currentBlock = this.blockchain[i];
        const precedingBlock = this.blockchain[i - 1];
  
        if (currentBlock.hash !== currentBlock.computeHash()) {
          return false;
        }
        if (currentBlock.precedingHash !== precedingBlock.hash) return false;
      }
      return true;
    }
  }

module.exports = { EarthChain };