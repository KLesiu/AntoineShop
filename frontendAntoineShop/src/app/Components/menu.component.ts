import { Component } from "@angular/core";


@Component({
    selector:'menu-component',
    standalone:true,
    imports:[],
    template:`
    <nav class="flex justify-between items-center w-full h-30">
        <ul class="flex justify-around w-1/5">
            <li>Men</li>
            <li>Woman</li>
            <li>Kids</li>
            <li>New & Featured</li>
        </ul>
        <h1>AntoineShop</h1>
        <div class="flex justify-around items-center w-1/12">
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