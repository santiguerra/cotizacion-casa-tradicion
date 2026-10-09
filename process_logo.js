const { Jimp } = require("jimp");

async function main() {
  const image = await Jimp.read("logo_metalevel.png");
  
  image.scan(0, 0, image.bitmap.width, image.bitmap.height, function (x, y, idx) {
    const r = this.bitmap.data[idx + 0];
    const g = this.bitmap.data[idx + 1];
    const b = this.bitmap.data[idx + 2];
    
    // Navy blue #1e3a8a => 30, 58, 138
    // Background is black, logo is white.
    if (r < 50 && g < 50 && b < 50) {
      // Make transparent
      this.bitmap.data[idx + 3] = 0;
    } else {
      // Make Navy
      const alpha = Math.max(r, g, b); // Use luminance as alpha for smooth edges
      this.bitmap.data[idx + 0] = 30; // R
      this.bitmap.data[idx + 1] = 58; // G
      this.bitmap.data[idx + 2] = 138; // B
      this.bitmap.data[idx + 3] = alpha; // Alpha
    }
  });

  await image.write("logo_navy.png");
  console.log("Done");
}
main().catch(console.error);
