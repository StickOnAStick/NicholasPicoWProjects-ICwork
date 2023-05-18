# NicholasPicoWProjects-ICwork
Collection of various hardware projects I've made this past year. Please also check the IC & Remote switch folder for IC projects and a remote switch I've made. *Note you will need logic works install to view the IC schematics functinality. Because of this I've also attached screenshots.  


# Skateboard
## Components used:
#### [PicoW](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
#### [Battery](https://www.aliexpress.us/item/3256805273114690.html?spm=a2g0o.productlist.main.1.1568661a9so3Wj&algo_pvid=edfec7ce-cdbd-4754-b9b0-7967948061da&algo_exp_id=edfec7ce-cdbd-4754-b9b0-7967948061da-0&pdp_npi=3%40dis%21USD%2125.65%2110.26%21%21%21%21%21%40211bc2a016844401366482899d0744%2112000033165595997%21sea%21US%210&curPageLogUid=8R5ggjKd3VNm)
#### [ESC](https://www.amazon.com/RioRand-6-60V-Brushless-Electric-Controller/dp/B087M2378D/ref=sr_1_fkmr0_2?crid=3K979OBXE0RUT&keywords=RioRand%2B350w&qid=1684440297&sprefix=riorand%2B350w%2Caps%2C125&sr=8-2-fkmr0&th=1)
#### [HC-05 Bluetooth Module](https://www.amazon.com/HiLetgo-Wireless-Bluetooth-Transceiver-Arduino/dp/B071YJG8DR/ref=sxin_16_pa_sp_search_thematic_sspa?content-id=amzn1.sym.0aa4d02f-da7d-419a-973d-b8a7d4190b28%3Aamzn1.sym.0aa4d02f-da7d-419a-973d-b8a7d4190b28&crid=X5VFJQY5ZNCW&cv_ct_cx=bluetooth+switch+module&keywords=bluetooth+switch+module&pd_rd_i=B071YJG8DR&pd_rd_r=4a160ca1-29ca-489d-a68b-c36113e01152&pd_rd_w=Lla9C&pd_rd_wg=W5VHI&pf_rd_p=0aa4d02f-da7d-419a-973d-b8a7d4190b28&pf_rd_r=7KN07TRM9G0HFCP69ZWW&qid=1684439826&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=bluetooth+switch+module%2Caps%2C149&sr=1-1-2b34d040-5c83-4b7f-ba01-15975dfb8828-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFUUlBHUUVGSEM0RzgmZW5jcnlwdGVkSWQ9QTAxMzIwMTkyRTNOQU5UUjZaNEdRJmVuY3J5cHRlZEFkSWQ9QTA2ODEwNTEyOVdNT0gwQllPMzJTJndpZGdldE5hbWU9c3Bfc2VhcmNoX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
#### [Motor](https://www.amazon.com/Electric-Skateboard-Brushless-Replacement-Longboard/dp/B084Q63QMK/ref=sr_1_30?crid=RRO7760MTUQA&keywords=skateboard+wheel+hub+motor&qid=1684440084&sprefix=skatboard+wheel+hub+motor%2Caps%2C145&sr=8-30)
#### [LM358 Op-Amp](https://www.ti.com/lit/ds/symlink/lm358.pdf?ts=1684437703728&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FLM358%253Futm_source%253Dsupplyframe%2526utm_medium%253DSEP%2526utm_campaign%253Dnot_alldatasheet%2526DCM%253Dyes%2526dclid%253DCKv_0qbL__4CFUyS1QodH0kIpQ)

## Funcitonality
 The current implimentation of the skateboard utilizes an app built uses MIT's (prev Google's) App Invetor to control the motor via communication via bluetooth. The current code only allows for full power or off; however, as I'm writing out these docs (5/18/23) I will also layout how I could add in PWM signaling for variable throttle control to the motor. 


## Power and control Wiring
Please refer to the Power and Control image for design specifics; however, here is a brief overview. 
#### Pico-W 
This microcontroller handles the main functionality for skateboards throttle control. The approach I took was to recieve a "Throttle On" signal from the HC-05. When the input arrives, we send out a 3.3V signal from Pin 34 into the LM358 OP-AMP (powered by 9v) to boost the signal to 5v, which is then sent to the ESC's variable potentiometer. Because we only can send 5v, the throttle control is limited to Full or Off. As mentioned earlier, I will be converting this to run the 5v signal into a DAC or other external device to convert the signal into a PWM signal that can vary the throttle, but for a prototype this worked fine. 

#### HC-05 
The bluetooth module communicates with a very basic app I built using MIT's App Inventor. The app sends out the aformentioned "Throttle On" signal which the HC-05 then transmits to the PicoW's UDART1 RX port. Power is supplied to this module via the PicoW; however, the HC-05 requires 3.6V and the PicoW is only capable of supplying 3.3V. Because of this, I've used the second channel on the LM358 to boost the signal 1.1x to 3.6V. 

#### ESC

The ESC I've chosen to use is capable of handling the massive 36v supplied by the battery and demanded by the motor for full power. The ESC was one of the few that I've found for less than $20 which was also equipped with an onboard hallsensor. Though it's currently not being used, I'd like to revise my design to add more accurate speed data and throttle control. That beign said, with the current implimentation I've been able to achieve aproximately 15mph and could likely go faster, though because I'm using a standard 8.25" deck with a narraw wheel base stability became a huge concern.   


### Troubles and things to change 

* Adding hall sensor functionality for accurate motor control
* Cleaning up the signals - The pico's signals (escpecially when powered by a 9v that's stepped down) are very noisy to say the least. This has led to many instances where the motor will suddenly cut out
* Adding variable throttle through the use of PWM signaling and alterations of the code
* Finding a seperate bluetooth remote that has a potentiometer for variable control (Tired of risking my phone just to skate 😅) 

