import { Component } from "@angular/core";


@Component({
    selector:'menu-component',
    standalone:true,
    imports:[],
    template:`
    <nav class="flex justify-between items-center w-full h-30">
        <ul class="flex justify-between w-1/5">
            <li>Men</li>
            <li>Woman</li>
            <li>Kids</li>
            <li>New & Featured</li>
        </ul>
        <h1 class="w-3/5 text-center text-4xl font-bold">AntoineShop</h1>
        <div class="flex justify-center gap-x-6 items-center w-1/5">
            <span class="material-symbols-outlined">search</span>
            <span class="material-symbols-outlined">shopping_basket</span>
            <span>Login</span>
        </div>

    </nav>
    `,
    styles:[]
})
export class MenuComponent{
 
}