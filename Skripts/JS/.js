/*Присвоение анимированным объектам класса _active для анимации
через css*/
const animItems = document.querySelectorAll('.anim-item');
if(animItems.length > 0)
{
	window.addEventListener('scroll', animOnScroll);
	/*Возвращает offset'ы*/
	function offset(el)
	{
		const rect = el.getBoundingClientRect(),
			scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
			scrollTop = window.pageYOffset || document.documentElement.scrollTop;
		return {top: rect.top + scrollTop, left: rect.left + scrollLeft}
	}
	/*Присвоение клласса, при скролле*/
	function animOnScroll()
	{
		let animItemPoint; //точка, когда объект начинает анимироваться
		for(let i = 0; i < animItems.length; i++)
		{
			//offsetHeight- высота элемента в пикселях, включая отступы.
			const animItem = animItems[i];
			const animItemHeight = animItem.offsetHeight;
			const animItemOffset = offset(animItem).top;
			const animStart = 0.25; //на сколько элемент должен появиться
									//для начала анимации

			//когда надо начинать анимировать
			animItemPoint = window.innerHeight - animItemHeight * animStart;

			//Ситуация, когда блок по высоте выше окна браузера
			if(animItemHeight > window.innerHeight){
				animItemPoint = window.innerHeight - window.innerHeight * animStart;
			}
			if((pageYOffset > animItemOffset - animItemPoint) &&
				pageYOffset < (animItemOffset + animItemHeight))
				animItem.classList.add('_active');
			else
				animItem.classList.remove('_active');
		}
	}
	//Запуск анимаций, при старте страницы
	animOnScroll();
}