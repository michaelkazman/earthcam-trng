const execSync = require('child_process').execSync;
const SHA256 = require("crypto-js/sha256");
const path = require('path');

class EarthBlock {
    constructor(index, timestamp, data, precedingHash = " ", hash) {
      this.index = index;
      this.timestamp = timestamp;
      this.data = data;
      this.precedingHash = precedingHash;
      this.nonce = 0
      this.hash = index ? null : this.computeHash()
    }
  
    computeNonce(difficulty) {
      const randomByteArray = execSync(`python3 ${path.resolve("./main.py")}`);
      const randomBytes = new Uint32Array(randomByteArray).slice(0, 5)
      const nonce = Number(randomBytes.join(""));
      return nonce
    }
  
    computeHash() {
      
      return SHA256(
        this.index +
          this.precedingHash +
          this.timestamp +
          JSON.stringify(this.data) +
          this.nonce
      ).toString();
    }
  
    proofOfWork(difficulty) {
      this.nonce = this.computeNonce();
      this.hash = this.computeHash();
      while (
        this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")
      ) {
        this.nonce++;
        this.hash = this.computeHash();
      }
    }
  }

module.exports = { EarthBlock };