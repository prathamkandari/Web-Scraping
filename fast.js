const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Set a custom user agent
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36');

    await page.goto('https://www.fastrack.in/store-locator/find');
    await page.waitForTimeout(3000);
    const htmlContent = await page.content();

    console.log(htmlContent);

    await browser.close();
})();
