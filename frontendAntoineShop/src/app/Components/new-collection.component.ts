import { Component } from "@angular/core";

@Component({
    selector:'new-collection-component',
    standalone:true,
    imports:[],
    template:`
        <section class="flex flex-col items-center mt-40">
            <h2 class="text-3xl font-bold">NEW COLLECTION</h2>
            <p class="text-gray-500">Our latest collection, where everyone can find someone for themselves</p>
            <div class="w-full h-auto flex justify-between gap-5 flex-wrap mt-5 ">
                <div class="w-96 h-72 bg-red-400"></div>
                <div class="w-96 h-72 bg-red-400"></div>
                <div class="w-96 h-72 bg-red-400"></div>
                <div class="w-96 h-72 bg-red-400"></div>
                <div class="w-96 h-72 bg-red-400"></div>
                <div class="w-96 h-72 bg-red-400"></div>
            </div>
        </section>
    `

})
export class NewCollectionComponent{}