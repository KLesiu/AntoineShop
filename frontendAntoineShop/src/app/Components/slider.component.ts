import { Component } from "@angular/core";

@Component({
    selector:"slider-component",
    standalone:true,
    imports:[],
    template:`
    <section class="w-4/5 mx-auto h-96 mt-10">
        <div class="w-full h-full bg-red-600 rounded-xl">image</div>
    </section>
    `,

})
export class SliderComponent{

}