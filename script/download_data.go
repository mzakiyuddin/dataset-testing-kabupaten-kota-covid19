package main

import (
	"fmt"
	"time"

	"github.com/go-rod/rod"
	"github.com/go-rod/rod/lib/proto"
	"github.com/go-rod/rod/lib/utils"
)

func main() {
	fmt.Println("Open link...")
	linkDashboard := "https://dashboard.kemkes.go.id/views/asesmenkabkotavaksinKTP2/Dtesting_kabkota"
	page := rod.New().MustConnect().MustPage(linkDashboard)
	time.Sleep(3 * time.Second)

	// Click Download Button
	fmt.Println("Click download first...")
	page.MustWaitLoad().MustElement("#download-ToolbarButton").MustClick()
	time.Sleep(3 * time.Second)

	// Click Crosstab
	fmt.Println("Click crosstab...")
	page.MustElement(`#DownloadDialog-Dialog-Body-Id > div > fieldset > button:nth-child(4)`).MustClick()
	time.Sleep(3 * time.Second)

	// Click Testing
	fmt.Println("Click csv testing...")
	page.MustElement("#export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id > div > div:nth-child(1) > div.f1lp596a > div > div > div:nth-child(3) > div").MustClick()
	time.Sleep(3 * time.Second)

	// Click download
	fmt.Println("Click download final...")
	page.MustElement("#export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id > div > div.fdr6v0d > button").MustClick()
	wait := page.MustWaitRequestIdle()
	wait()

	list, err := proto.PageGetResourceTree{}.Call(page)
	utils.E(err)

	data, err := page.GetResource(list.FrameTree.Frame.URL)
	utils.E(err)

	utils.E(utils.OutputFile("my.xlsx", data))

	fmt.Println("Waiting 5 second...")
	time.Sleep(8 * time.Second)
}
