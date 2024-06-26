package main

import (
	"fmt"
	"time"

	"github.com/go-rod/rod"
	"github.com/go-rod/rod/lib/utils"
)

func main() {
	fmt.Println("Open link...")
	linkDashboard := "https://dashboard.kemkes.go.id/views/asesmenkabkotavaksinKTP2/Dtesting_kabkota?%3Aembed=y&%3AisGuestRedirectFromVizportal=y"
	page := rod.New().MustConnect().MustPage(linkDashboard)
	time.Sleep(3 * time.Second)

	// Click Download Button
	fmt.Println("Click download first...")
	page.MustWaitLoad().MustElement("#download").MustClick()
	time.Sleep(3 * time.Second)

	// Click Crosstab
	fmt.Println("Click crosstab...")
	page.MustElementR(`label`, "Crosstab").MustClick()
	time.Sleep(3 * time.Second)

	// Click Testing
	fmt.Println("Click csv testing...")
	page.MustElement("#export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id > div > div:nth-child(1) > div.f1lp596a > div > div > div:nth-child(3) > div").MustClick()
	time.Sleep(3 * time.Second)

	// Click download
	fmt.Println("Click download final...")
	wait := page.Browser().MustWaitDownload()

	page.MustElement("#export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id > div > div.fdr6v0d > button").MustClick()
	_ = utils.OutputFile("data/temp/temp.xlsx", wait())

}
