import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { MenuComponent } from './Components/menu.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet,MenuComponent],
  template: `
  <div class="max-w-7xl flex justify-center mx-auto">
      <menu-component class="w-full"/>
  </div>
  `,
  styles:[]
})
export class AppComponent {
  title = 'AntoineShop';
}
