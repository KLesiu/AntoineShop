import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { MenuComponent } from './Components/menu.component';
import { SliderComponent } from './Components/slider.component';
import { NewCollectionComponent } from './Components/new-collection.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet,MenuComponent,SliderComponent,NewCollectionComponent],
  template: `
  <div class="max-w-7xl flex justify-center mx-auto flex-wrap">
      <menu-component class="w-full"/>
      <slider-component class="w-full"/>
      <new-collection-component class="w-full" />

  </div>
  `,
  styles:[]
})
export class AppComponent {
  title = 'AntoineShop';
}
