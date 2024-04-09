#!/usr/bin/node

module.exports = class Rectsngle {
        constructor(w, h) {
                if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h) {
                        return 0;
                } else {
                        this.width = w;
                        this.height = h;
                }
        }
        print() {
                for (let i = 0; i < this.height; i++) {
                        console.log('x'.repeat(this.width));
                }
        }
	 rotate () {
		 [this.width, this.height] = [this.height, this.width];
	 }
	double () {
		[this.width, this.height] = [this.width * 2, this.height * 2];
	}
};
