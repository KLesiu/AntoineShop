import { Component } from "@angular/core";

@Component({
    selector:'main-page-nav-component',
    standalone:true,
    imports:[],
    template:`
    <section class="w-full flex justify-between mt-40 flex-wrap ">
        <h2 class="w-full text-4xl text-center font-bold mb-5  p-10">WHO ARE YOU?</h2>
        <div class="bg-red-500 w-xl h-96 rounded-xl flex justify-end pb-5 pl-5 flex-wrap flex-col">
            <h3 class="w-2/5 text-center text-xl mb-2">MAN</h3>
            <button class="w-2/5 bg-white rounded-2xl h-10">See Details</button>
        </div>
        <div class="bg-red-500 w-xl h-96 rounded-xl flex justify-end pb-5 pl-5 flex-wrap flex-col">
            <h3 class="w-2/5 text-center text-xl mb-2">WOMAN</h3>
            <button class="w-2/5 bg-white rounded-2xl h-10">See Details</button>
        </div>
        <div class="bg-red-500 w-xl h-96 rounded-xl flex justify-end pb-5 pl-5 flex-wrap flex-col">
            <h3 class="w-2/5 text-center text-xl mb-2">KIDS</h3>
            <button class="w-2/5 bg-white rounded-2xl h-10">See Details</button>
        </div>
    </section>
    `,
})
export class MainPageNavComponent{

}